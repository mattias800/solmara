// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// One project for Solmara's website and its manual, served on GitHub Pages
// at /solmara/. The website's pages are in src/pages; the manual is
// Starlight's, from src/content/docs/manual, at /solmara/manual/.
export default defineConfig({
	site: 'https://mattias800.github.io',
	base: '/solmara',
	trailingSlash: 'always',
	integrations: [
		starlight({
			title: 'Solmara manual',
			description: 'How to make music with Solmara.',
			logo: { src: './src/assets/mark.svg', replacesTitle: false },
			favicon: '/favicon.svg',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/mattias800/solmara' }],
			customCss: ['./src/styles/manual.css'],
			components: { SiteTitle: './src/components/ManualTitle.astro' },
			head: [
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true } },
				{
					tag: 'link',
					attrs: {
						rel: 'stylesheet',
						href: 'https://fonts.googleapis.com/css2?family=Cormorant:wght@500;600&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400&display=swap',
					},
				},
			],
			sidebar: [
				{ label: 'Welcome', slug: 'manual' },
				{
					label: 'Learn',
					items: [{ label: 'Your first song', slug: 'manual/learn/first-song' }],
				},
				{
					label: 'Understand',
					items: [
						{ label: 'The editor at a glance', slug: 'manual/concepts/editor' },
						{ label: 'How clips loop', slug: 'manual/concepts/looping' },
					],
				},
				{
					label: 'How to',
					items: [
						{
							label: 'Arrange',
							items: [
								{ label: 'Tracks', slug: 'manual/guides/tracks' },
								{ label: 'Work with clips', slug: 'manual/guides/clips' },
								{ label: 'Tempo, time and markers', slug: 'manual/guides/tempo-and-markers' },
								{ label: 'Play clips live in the session', slug: 'manual/guides/session' },
								{ label: 'Automate a sound', slug: 'manual/guides/automation' },
							],
						},
						{
							label: 'Write',
							items: [
								{ label: 'Write notes in the piano roll', slug: 'manual/guides/piano-roll' },
								{ label: 'Compose with chords', slug: 'manual/guides/composer' },
								{ label: 'Drum and step patterns', slug: 'manual/guides/drum-patterns' },
								{ label: 'MIDI devices', slug: 'manual/guides/midi-devices' },
								{ label: 'Trackers and modules', slug: 'manual/guides/tracker' },
							],
						},
						{
							label: 'Sound',
							items: [
								{ label: 'Devices and presets', slug: 'manual/guides/devices' },
								{ label: 'Vintergatan, the flagship synth', slug: 'manual/guides/vintergatan' },
								{ label: 'Samplers', slug: 'manual/guides/samplers' },
								{ label: 'The Modular', slug: 'manual/guides/modular' },
								{ label: 'Guitar and bass', slug: 'manual/guides/guitar' },
								{ label: 'The library and sounds', slug: 'manual/guides/library' },
							],
						},
						{
							label: 'Record and audio',
							items: [
								{ label: 'Record', slug: 'manual/guides/recording' },
								{ label: 'Audio clips', slug: 'manual/guides/audio-clips' },
							],
						},
						{
							label: 'Mix and finish',
							items: [
								{ label: 'Mix', slug: 'manual/guides/mixing' },
								{ label: 'Master a song', slug: 'manual/guides/mastering' },
								{ label: 'Save and export', slug: 'manual/guides/projects' },
							],
						},
						{
							label: 'AI and agents',
							items: [
								{ label: 'AI on your own computer', slug: 'manual/guides/ai' },
								{ label: 'Make music with an agent', slug: 'manual/guides/agents' },
							],
						},
					],
				},
				{
					label: 'Reference',
					items: [
						{ label: "Arrangement: mouse and keys", slug: 'manual/reference/arrangement-mouse-and-keys' },
						{ label: 'Keyboard shortcuts', slug: 'manual/reference/keyboard-shortcuts' },
						{ label: 'Preferences', slug: 'manual/reference/preferences' },
					],
				},
				{
					label: 'Devices',
					collapsed: true,
					items: [
						{ label: 'Instruments', collapsed: true, items: [{ autogenerate: { directory: 'manual/devices/instruments' } }] },
						{ label: 'Effects', collapsed: true, items: [{ autogenerate: { directory: 'manual/devices/effects' } }] },
						{ label: 'Guitar and bass', collapsed: true, items: [{ autogenerate: { directory: 'manual/devices/guitar' } }] },
						{ label: 'MIDI devices', collapsed: true, items: [{ autogenerate: { directory: 'manual/devices/midi' } }] },
					],
				},
				{ label: '← The Solmara website', link: '/' },
			],
		}),
	],
});
