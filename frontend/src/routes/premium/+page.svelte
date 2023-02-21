<script>
	import Card from '../../components/Card.svelte';

	let courses = [
		{
			title: 'FastAPI für Anfänger - Baue einen Twitter Clone mit FastAPI',
			video: 'images/kurse/fastapi_tut.jpg',
			link: 'https://www.udemy.com/course/fastapi-fur-anfanger-baue-einen-twitter-clone-mit-fastapi/',
			description:
				'In diesem Kurs lernst du die Grundlagen des beliebten Python-Frameworks FastAPI. Dieser Kurs macht dich Schritt für Schritt zu einem kompetenten Entwickler für APIs mit Python.'
		},
		{
			title: 'Data Wrangling mit dem Tidyverse',
			video: 'images/kurse/rprog_tut.jpg',
			link: 'https://www.udemy.com/course/data-wrangling-mit-dem-tidyverse/',
			description:
				'Das Tidyverse ist eine Sammlung von Libraries, die das Data Wrangling mit R vereinfachen und das Arbeiten mit Daten deutlich angenehmer gestalten. Du wirst lernen, wie du die wesentlichen Funktionen dieser Libraries anwendest und dich Schritt für Schritt damit vertraut machen'
		}
	];
	let programmieren_starten = [
		{
			title: 'FastAPI für Anfänger - Baue einen Twitter Clone mit FastAPI',
			video: 'images/kurse/fastapikurs.svg',
			link: 'https://programmieren-starten.de/fastapi-lp1/',
			description:
				'In diesem Kurs lernst du die Grundlagen des beliebten Python-Frameworks FastAPI. Dieser Kurs macht dich Schritt für Schritt zu einem kompetenten Entwickler für APIs mit Python.'
		}
	];
</script>

<div class="wrapper bg-blue-200 pb-20 p-4 text-center">
	<div class="max-w-screen-xl mx-auto pt-40 bg">
		<h1 class="text-black text-4xl font-extrabold">Meine Premium Kurse</h1>
		<div class="py-4 text-xl text-center px-8">
			<p>Hier findest du eine Übersicht über meine Premium Kurse. Diese Kurse befassen sich im Gegensatz zu meinen eher kürzeren Videos auf YouTube in-depth mit den unten aufgeführten Themen. Weitere Kurse sind bereits in Arbeit!</p>
		</div>
		<h2 class="text-black text-2xl py-6 font-bold">Udemy</h2>
		<div class="cardwrapper grid grid-cols-1 md:grid-cols-2 gap-6">
			{#each courses as course}
				<Card video_id={course.video} link={course.link} title={course.title}>
					<div slot="description" class="pb-8 text">
						<p class="text-left">{course.description}</p>
					</div>
				</Card>
			{/each}
		</div>
		<h2 class="text-black text-2xl py-10 font-bold">Programmieren starten</h2>
		<div class="cardwrapper grid grid-cols-1 md:grid-cols-2 gap-6">
			{#each programmieren_starten as course}
				<Card video_id={course.video} link={course.link} title={course.title}>
					<div slot="description" class="pb-8 text">
						<p class="text-left">{course.description}</p>
					</div>
				</Card>
			{/each}
		</div>
	</div>
</div>

<style>
	.wrapper {
		min-height: calc(100vh - 40px);
	}
</style>
