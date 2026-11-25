// Solmara's devices as the website shows them: what scripts/devices.py
// exported from the app, with the hand-written words of blurbs.json and the
// choices of site.json laid over it.
import type { ImageMetadata } from 'astro';
import exported from '../data/devices.json';
import blurbs from '../data/blurbs.json';
import site from '../data/site.json';

export interface Device {
	id: string;
	slug: string;
	label: string;
	kind: 'instrument' | 'effect' | 'midi';
	group: string | null;
	part: string | null;
	tag: string | null;
	summary: string | null;
	description: string | null;
	window: boolean;
	sidechain: boolean;
	controls: number;
	face: string | null;
}

export interface Shown extends Device {
	/** What it is, in a few words: the hand-written kind, or the app's tag. */
	kindLabel: string;
	/** One or two sentences for a card. */
	blurb: string;
	inProgress: boolean;
	image: ImageMetadata | null;
}

const faces = import.meta.glob<{ default: ImageMetadata }>('../assets/devices/*.webp', { eager: true });
const handWritten = blurbs as Record<string, { kind: string | null; text: string | null }>;

const sentence = (text: string) => text.charAt(0).toUpperCase() + text.slice(1) + (/[.!?]$/.test(text) ? '' : '.');

function shown(device: Device): Shown {
	const words = handWritten[device.label];
	const summary = device.summary ? sentence(device.summary) : '';
	return {
		...device,
		kindLabel: words?.kind ?? (device.tag ? sentence(device.tag).replace(/\.$/, '') : device.group ?? ''),
		blurb: words?.text ?? summary,
		inProgress: site.inProgress.includes(device.id),
		image: device.face ? (faces[`../assets/devices/${device.face}.webp`]?.default ?? null) : null,
	};
}

const hidden = new Set(site.hidden);
export const devices: Shown[] = (exported as Device[])
	.filter((device) => !hidden.has(device.id))
	.map(shown)
	.sort((a, b) => a.label.localeCompare(b.label));

export const byId = (id: string) => devices.find((device) => device.id === id);

const matches = (device: Shown, match: Record<string, string>) =>
	Object.entries(match).every(([field, value]) => (device as unknown as Record<string, unknown>)[field] === value);

export const instruments = devices.filter((device) => device.kind === 'instrument');
export const instrumentFamilies = site.instrumentFamilies.map((family) => ({
	...family,
	devices: instruments.filter((device) => matches(device, family.match)),
}));
export const familyOf = (device: Shown) => instrumentFamilies.find((family) => family.devices.includes(device));

export const effects = devices.filter((device) => device.kind === 'effect' && device.group !== 'Guitar & bass');
export const effectFamilies = site.effectFamilies.map((family) => ({
	...family,
	devices: effects.filter((device) => device.group === family.group),
}));

export const guitar = devices.filter((device) => device.group === 'Guitar & bass');
export const guitarFamilies = site.guitarFamilies.map((family) => ({
	...family,
	devices: guitar.filter((device) => device.part === family.part),
}));

export const midiDevices = devices.filter((device) => device.kind === 'midi');
export const mastering = site.mastering.map(byId).filter((device): device is Shown => Boolean(device));

/** Where a device is shown on the website: its own page, or its place on its family's. */
export function pageOf(device: Shown, base: string): string {
	const root = base.replace(/\/$/, '');
	if (device.kind === 'instrument') return `${root}/instruments/${device.slug}/`;
	if (device.kind === 'midi') return `${root}/write/#${device.slug}`;
	if (device.group === 'Guitar & bass') return `${root}/guitar/#${device.slug}`;
	return `${root}/effects/#${device.slug}`;
}

export const counts = {
	all: devices.length,
	instruments: instruments.length,
	effects: effects.length,
	guitar: guitar.length,
	midi: midiDevices.length,
};
