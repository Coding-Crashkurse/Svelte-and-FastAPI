img
<script>
    import Card from "../../components/Card.svelte";
</script>

<div class="wrapper bg-blue-200 pb-20 p-4">
    <div class="max-w-screen-xl mx-auto pt-40 bg">
        <h1 class="text-black text-center text-3xl md:text-4xl font-extrabold mb-4">Meine Crashkurse auf YouTube</h1>
        <div>
            <div class="logos flex gap-6 md:gap-16 flex-column mt-16 justify-center">
                <img src="images/html.png" alt="" class="object-cover w-16 md:w-24 h-16 md:h-24">
                <img src="images/css.png" alt="" class="object-cover w-16 md:w-24 h-16 md:h-24">
                <img src="images/javascript.png" alt="" class="object-cover w-16 md:w-24 h-16 md:h-24">
                <img src="images/python.png" alt="" class="object-cover w-16 md:w-24 h-16 md:h-24">
                <img src="images/typescript.png" alt="" class="object-cover w-16 md:w-24 h-16 md:h-24">
            </div>
            <div class="flex justify-end p-4">
                <h2 class="text-xl">... und mehr</h2>
            </div>

        </div>

        <div class="cardwrapper grid md:grid-cols-3 grid-cols-1 gap-6">
            <Card/>
            <Card/>
            <Card/>
            <Card/>
            <Card/>
            <Card/>
            <Card/>
            <Card/>
        </div>
</div>


</div>





