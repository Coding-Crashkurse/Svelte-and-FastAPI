<script lang="ts">
    import Card from '../../components/Card.svelte';

    /** @type {import('./$types').PageData} */
    export let data;

    // Always display all courses without reversing the order
    const dataToBeShown = data.courses;
</script>

<div class="wrapper bg-blue-200 pb-20 p-4 text-center">
    <div class="max-w-screen-xl mx-auto pt-40 bg">
        <h1 class="text-black text-4xl font-extrabold">My Premium Courses</h1>
        <div class="py-4 text-xl text-center px-8">
            <p>Here you will find an overview of my premium courses. Unlike my shorter videos on YouTube, these courses delve in-depth into the topics listed below. More courses are already in the works!</p>
        </div>
        <h2 class="text-black text-2xl py-6 font-bold">Udemy</h2>
        <div class="cardwrapper grid grid-cols-1 md:grid-cols-2 gap-6">
            {#each dataToBeShown as course (course.id)}
                <Card video_id={course.video} link={course.link} title={course.title} active_promotion={course.active_promotion} promo_until={course.promo_until}>
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
