<script lang="ts">
  export let image_url: string;
  export let description: string;
  export let link: string;
  export let title: string;

</script>


<div class="card w-full bg-base-100 shadow-xl">
    <figure><img src={image_url} alt="Shoes" /></figure>
    <div class="card-body">
      <h2 class="card-title">{title}</h2>
      <p>{description}</p>
      <div class="card-actions justify-end">
        <a target="_blank" rel="noreferrer" href={link} class="btn bg-blue-700 hover:bg-blue-800">Jetzt ansehen</a>
      </div>
    </div>
  </div>