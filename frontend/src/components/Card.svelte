<script lang="ts">
	export let video_id: string;
	export let link: string;
	export let title: string;
</script>

<a target="_blank" rel="noreferrer" href={link}>
	<div class="card w-full bg-base-100 shadow-xl">
		<figure><img src={video_id} alt="Shoes" /></figure>
		<div class="card-body text md:h-80">
			<h3 class="card-title pt-4 pb-10">{title}</h3>
			<slot name="description" />
		</div>
	</div>
</a>
