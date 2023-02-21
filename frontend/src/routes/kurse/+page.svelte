<script lang="ts">
	import Card from '../../components/Card.svelte';

	let show_all = false;
	export let data: Array<{
		id: number;
		video_id: string;
		link: string;
		title: string;
	}> = [];

	$: arr = Object.values(data);
	$: dataToBeShown = show_all ? arr : arr.slice(0, 9);
</script>

<div class="wrapper bg-blue-200 pb-20 p-4">
	<div class="max-w-screen-xl mx-auto pt-40 bg">
		<h1 class="text-black text-center text-3xl md:text-4xl font-extrabold mb-4">
			Meine Crashkurse auf YouTube
		</h1>
		<div class="py-4 text-xl text-center px-8">
			<p>Frontend? Backend? Projekte? Oder eher theoretisch? Kein Problem!</p>
			<p>Hier findest du eine umfangreiche Auswahl an Videos zu verschiedenen Themen.</p>
		</div>


		<div>
			<div class="logos flex gap-6 md:gap-16 flex-column mt-16 justify-center">
				<img src="images/html.png" alt="" class="object-cover w-12 md:w-24 h-12 md:h-24" />
				<img src="images/css.png" alt="" class="object-cover w-12 md:w-24 h-12 md:h-24" />
				<img src="images/javascript.png" alt="" class="object-cover w-12 md:w-24 h-12 md:h-24" />
				<img src="images/python.png" alt="" class="object-cover w-12 md:w-24 h-12 md:h-24" />
				<img src="images/typescript.png" alt="" class="object-cover w-12 md:w-24 h-12 md:h-24" />
			</div>
			<div class="flex justify-end p-4">
				<h2 class="text-xl">... und mehr</h2>
			</div>
		</div>

		<div class="cardwrapper grid md:grid-cols-3 grid-cols-1 gap-6">
			{#each dataToBeShown as item (item.video_id)}
				<Card {...item} />
			{/each}
		</div>
		<div class="flex mt-6">
			<button
				class="btn mx-auto w-30"
				on:click={() => {
					show_all = !show_all;
				}}>{show_all ? 'Verstecken...' : 'Alle anzeigen...'}</button
			>
		</div>
	</div>
</div>
