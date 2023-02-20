<div class="wrapper bg-blue-200 pb-20">
	<div class="max-w-screen-xl mx-auto pt-40 bg">
		<h1 class="text-black text-4xl font-extrabold mb-4 text-center">Über mich</h1>
		<div class="flex gap-8 flex-col md:flex-row p-4">
			<div class="logoborder-1 shrink-0 flex justify-center">
				<img src="/images/profil.JPG" alt="" class="border-2 border-white rounded-xl w-72" />
			</div>
			<div class="links p-8 text-white bg-gray-800 rounded-xl self-start">
				<p class="py-2">
					Hallo, mein Name ist <span class="text-blue-400">Markus</span>. Ich bin Softwareentwickler
					im KI Bereich, bin auf Python spezialisiert, bin aber auch gerne im Frontend unterwegs und
					probiere mich an JavaScript Frameworks. Zudem arbeite ich auch gerne mit Container
					Technologien wie Docker & Kubernetes.
				</p>
				<p class="py-2">
					2021 habe ich meinen YouTube Kanal "Coding Crashkurse" gegründet und teile seitdem mein
					Wissen mit anderen.
				</p>
				<p class="py-2">
					Da ich selbst "self-taught" bin, ist es mir gerade ein Anliegen auch anderen
					Quereinsteigern zu zeigen, wie man ohne Informatikstudium in die IT kommt.
				</p>
			</div>
		</div>
		<div class="py-8 ">
			<h1 class="text-black text-4xl font-extrabold my-10 text-center">Über dieses Projekt</h1>
			<div class="project-wrapper flex justify-around text-center flex-col md:flex-row">
				<div class="frontend flex-1 py-10">
					<h2 class="text-3xl md:text-2xl font-bold pb-4">Frontend</h2>
					<img src="images/sveltelogo.png" alt="" class="w-36 mx-auto p-2" />
					<img src="images/tailwind.png" alt="" class="w-44 mx-auto p-2" />
				</div>
				<div class="backend flex-1 py-10">
					<h3 class="text-3xl md:text-2xl font-bold pb-4">Backend</h3>
					<img src="images/fastapi.png" alt="" class="w-100 mx-auto p-2" />
					<img src="images/postgres.png" alt="" class="w-40 mx-auto p-2" />
				</div>
				<div class="hosting flex-1 py-10">
					<h3 class="text-3xl md:text-2xl font-bold pb-4">Deployment & Hosting</h3>
					<img src="images/docker.png" alt="" class="w-52 mx-auto p-2" />
					<img src="images/digitalocean.png" alt="" class="w-48 mx-auto p-2" />
				</div>
			</div>
			<!-- <div class="text-center">
                        <p class="italic mt-8">Weitere Informationen:</p>
                        <p>Dieses Produkt ist veröffentlicht unter der MIT Lizenz.</p>
                    <div>
                            Code: <a href="https://github.com/Coding-Crashkurse/Svelte-and-PocketBase" target="_blank" rel="noreferrer">Repository</a>
                    </div>
                </div> -->
		</div>
	</div>
</div>

<style>
	.wrapper {
		min-height: calc(100vh - 40px);
	}
</style>
