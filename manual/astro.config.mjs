// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// The manual is served beside the website, at /solmara/manual/ on GitHub
// Pages; the Pages workflow builds it into site/manual.
export default defineConfig({
	site: 'https://mattias800.github.io',
	base: '/solmara/manual',
	integrations: [
		starlight({
			title: 'Solmara manual',
			description: 'How to make music with Solmara.',
			logo: { src: './src/assets/mark.svg', replacesTitle: false },
			favicon: '/favicon.svg',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/mattias800/solmara' }],
			customCss: ['./src/styles/solmara.css'],
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
				{ label: 'Welcome', slug: '' },
				{
					label: 'How to',
					items: [
						{ label: 'Work with clips', slug: 'guides/clips' },
						{ label: 'Automate a sound', slug: 'guides/automation' },
					],
				},
				{
					label: 'Understand',
					items: [{ label: 'How clips loop', slug: 'concepts/looping' }],
				},
				{
					label: 'Reference',
					items: [{ label: 'Arrangement: mouse and keys', slug: 'reference/arrangement-mouse-and-keys' }],
				},
			],
		}),
	],
});
