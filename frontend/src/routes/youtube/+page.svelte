
<script>
    import Card from "../../components/Card.svelte";
</script>

<div class="wrapper bg-blue-200 pb-20">
    <div class="max-w-screen-xl mx-auto pt-40 bg">
        <h1 class="text-black text-4xl font-extrabold mb-4">Meine Crashkurse auf YouTube</h1>
        <div>
            <div class="logos flex gap-12 flex-column mt-12 justify-center">
                <img src="images/html.png" alt="" class="object-cover w-24 h-24">
                <img src="images/css.png" alt="" class="object-cover w-24 h-24">
                <img src="images/javascript.png" alt="" class="object-cover w-24 h-24">
                <img src="images/python.png" alt="" class="object-cover w-24 h-24">
                <img src="images/typescript.png" alt="" class="object-cover w-24 h-24">
            </div>
            <div class="flex justify-end p-4">
                <h2 class="text-xl">... und mehr</h2>
            </div>

        </div>

        <div class="cardwrapper grid grid-cols-3 gap-6">
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





