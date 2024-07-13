<script lang="ts">
    import Card from '../../components/Card.svelte';

    /** @type {import('./$types').PageData} */
    export let data;

    let show_all = false;

    $: dataToBeShown = show_all ? [...data.courses].reverse() : [...data.courses].slice(0, 9).reverse();

</script>

<div class="wrapper bg-blue-200 pb-20 p-4">
    <div class="max-w-screen-xl mx-auto pt-40 bg">
        <h1 class="text-black text-center text-3xl md:text-4xl font-extrabold mb-4">
            My Crash Courses on YouTube
        </h1>
        <div class="py-4 text-xl text-center px-8">
            <p>Frontend? Backend? Projects? AI? Or more theoretical? No problem!</p>
            <p>Here you will find a comprehensive selection of videos on various topics.</p>
        </div>

        <div>
            <div class="logos flex gap-6 md:gap-16 flex-column mt-16 justify-center">
                <img src="images/html.png" alt="HTML logo" class="object-cover w-12 md:w-24 h-12 md:h-24" />
                <img src="images/css.png" alt="CSS logo" class="object-cover w-12 md:w-24 h-12 md:h-24" />
                <img src="images/javascript.png" alt="JavaScript logo" class="object-cover w-12 md:w-24 h-12 md:h-24" />
                <img src="images/python.png" alt="Python logo" class="object-cover w-12 md:w-24 h-12 md:h-24" />
                <img src="images/typescript.png" alt="TypeScript logo" class="object-cover w-12 md:w-24 h-12 md:h-24" />
            </div>
            <div class="flex justify-end p-4">
                <h2 class="text-xl">... and more</h2>
            </div>
        </div>

        <div class="cardwrapper grid md:grid-cols-3 grid-cols-1 gap-6">
            {#each dataToBeShown as item (item.id)}
                <Card video_id={item.video_id} link={item.link} title={item.title} />
            {/each}
        </div>
        <div class="flex mt-6">
            <button
                class="btn mx-auto w-30"
                on:click={() => {
                    show_all = !show_all;
                }}>{show_all ? 'Hide...' : 'Show all...'}</button
            >
        </div>
    </div>
</div>
