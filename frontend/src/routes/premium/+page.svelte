<script>
  import Card from "../../components/Card.svelte";

  let courses = [
    {
      title: "FastAPI für Anfänger - Baue einen Twitter Clone mit FastAPI",
      description: "6 Stunden in-depth Kurs zum beliebsten Python Framework zur Entwicklung von RestAPIs",
      video: "images/kurse/fastapi_tut.jpg",
      link: "https://www.udemy.com/course/fastapi-fur-anfanger-baue-einen-twitter-clone-mit-fastapi/",
    },
    {
      title: "Data Wrangling mit dem Tidyverse",
      description: "Lerne die nötigen Skills um deine Datensätze zu bändigen",
      video: "images/kurse/rprog_tut.jpg",
      link: "https://www.udemy.com/course/data-wrangling-mit-dem-tidyverse/",
    },
  ];
</script>

<div class="wrapper bg-blue-200 pb-20 h-screen p-4 text-center">
  <div class="max-w-screen-xl mx-auto pt-40 bg">
    <h1 class="text-black text-4xl font-extrabold mb-4">Meine Premium Kurse</h1>
    <div class="cardwrapper grid grid-cols-1 md:grid-cols-2 gap-6">
      {#each courses as course}
        <Card
          video_id={course.video}
          description={course.description}
          link={course.link}
          title={course.title}
        />
      {/each}
    </div>
  </div>
</div>
