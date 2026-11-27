// The manual's Devices, as the app's browser groups them: each section a
// folder of chapters under src/content/docs/manual/devices and a group of
// the sidebar, in this order. scripts/manual_devices.py files the chapters
// by the same rule (manual_folder); keep the two alike.

export const deviceSections = [
	['Analog synths', 'analog-synths'],
	['Digital synths', 'digital-synths'],
	['Drums', 'drums'],
	['Keys', 'keys'],
	['Samplers', 'samplers'],
	['Delay and reverb', 'delay-and-reverb'],
	['Dynamics', 'dynamics'],
	['EQ and filters', 'eq-and-filters'],
	['Pedals', 'pedals'],
	['Guitar amps', 'guitar-amps'],
	['Bass amps', 'bass-amps'],
	['Cabs', 'cabs'],
	['Modulation', 'modulation'],
	['Pitch', 'pitch'],
	['Preamps and channels', 'preamps-and-channels'],
	['Saturation', 'saturation'],
	['Utilities', 'utilities'],
	['MIDI devices', 'midi'],
];

const folderOf = (name) => name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

/** The folder a device's chapter stands in: its section's. */
export function manualFolder(device) {
	if (device.kind === 'midi') return 'midi';
	if (device.id === 'builtin.modular') return 'modular';
	if (device.group === 'Guitar & bass') return folderOf(device.part ?? 'other');
	if (device.group === 'Synths') return folderOf(`${device.part ?? 'other'} synths`);
	return folderOf(device.group ?? 'other');
}

/** Where its chapter stood before the sections, for the redirects: none where it has not moved. */
export function formerFolders(device) {
	if (device.kind === 'midi') return [];
	if (device.kind === 'instrument') return ['instruments'];
	if (device.group === 'Guitar & bass') {
		const part = { 'Guitar amps': 'amps', 'Bass amps': 'bass-amps', Pedals: 'pedals', Cabs: 'cabs' }[device.part];
		return part ? ['guitar', `guitar/${part}`] : ['guitar'];
	}
	return ['effects'];
}
