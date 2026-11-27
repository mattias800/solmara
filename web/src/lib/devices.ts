// Solmara's devices as the website shows them: what scripts/devices.py
// exported from the app, with the hand-written words of blurbs.json and the
// choices of site.json laid over it.
import type { ImageMetadata } from 'astro';
import exported from '../data/devices.json';
import blurbs from '../data/blurbs.json';
import site from '../data/site.json';
import origins from '../data/origins.json';
import opensData from '../data/opens.json';

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
	/** A design of Solmara's own, or an emulation of other gear or software. */
	origin: Origin;
	/** For an emulation, what it is modeled on, never by its maker's or its model's name. */
	modeledOn: string | null;
	/** The presets of other instruments it opens (interoperability, where products are named). */
	opens: string | null;
}

// 'unsaid' for a device whose origin the website does not tell: the MIDI
// players, which follow another DAW's functions closely and are neither
// called our own nor said to be modeled on software.
export type Origin = 'own' | 'analog' | 'digital' | 'unsaid';
/** The three parts every family's devices are shown in, in this order. */
export const originParts: { key: Origin; label: string; short: string }[] = [
	{ key: 'own', label: 'Our own designs', short: 'Our own design' },
	{ key: 'analog', label: 'Emulations of analog gear', short: 'Analog emulation' },
	{ key: 'digital', label: 'Emulations of digital gear', short: 'Digital emulation' },
];
export const originLabel = (origin: Origin) => originParts.find((part) => part.key === origin)?.short ?? '';
/** A family's devices in its three parts, the empty ones left out. */
export const byOrigin = (list: Shown[]) =>
	originParts.map((part) => ({ ...part, devices: list.filter((device) => device.origin === part.key) })).filter((part) => part.devices.length > 0);

const faces = import.meta.glob<{ default: ImageMetadata }>('../assets/devices/*.webp', { eager: true });
const handWritten = blurbs as Record<string, { kind: string | null; text: string | null }>;
const opens = opensData as unknown as Record<string, { text: string }>;
const emulations = origins.emulations as Record<string, { circuit: 'analog' | 'digital'; modeledOn: string }>;

const sentence = (text: string) => text.charAt(0).toUpperCase() + text.slice(1) + (/[.!?]$/.test(text) ? '' : '.');
/** The first sentence of the app's longer description, for a device with no shorter words. */
const firstSentence = (text: string | null) => {
	if (!text) return '';
	const plain = text.replace(/^A MIDI device: /, '');
	const end = plain.search(/\.(\s|$)/);
	return sentence(end > 0 ? plain.slice(0, end) : plain);
};

function shown(device: Device): Shown {
	const words = handWritten[device.label];
	const summary = device.summary ? sentence(device.summary) : '';
	return {
		...device,
		kindLabel: words?.kind ?? (device.tag ? sentence(device.tag).replace(/\.$/, '') : device.group ?? ''),
		blurb: words?.text ?? (summary || firstSentence(device.description)),
		inProgress: site.inProgress.includes(device.id),
		image: device.face ? (faces[`../assets/devices/${device.face}.webp`]?.default ?? null) : null,
		origin: device.kind === 'midi' ? 'unsaid' : (emulations[device.id]?.circuit ?? 'own'),
		modeledOn: emulations[device.id]?.modeledOn ?? null,
		opens: opens[device.id]?.text ?? null,
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
	if (device.id === 'builtin.modular') return `${root}/modular/`;
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
