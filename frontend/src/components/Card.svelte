<script lang="ts">
	export let video_id: string;
	export let link: string;
	export let title: string;
</script>

<div class="card w-full bg-base-100 shadow-xl">
	<figure><img src={video_id} alt="Shoes" /></figure>
	<div class="card-body text">
		<h3 class="card-title pt-4 pb-10">{title}</h3>
		<slot name="description" />
		<div class="card-actions justify-end">
			<a target="_blank" rel="noreferrer" href={link} class="btn bg-blue-700 hover:bg-blue-800"
				>Jetzt ansehen</a
			>
		</div>
	</div>
</div>
