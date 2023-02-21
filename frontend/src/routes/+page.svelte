<div class="wrapper">
	<div class="max-w-screen-xl mx-auto pt-40">
		<div class="text-center hidden md:block">
			<h3 class="text-blue-500 text-2xl p-2 uppercase font-extrabold">Coding Crashkurse</h3>
			<h1 class="text-6xl text-white p-4 uppercase font-extrabold leading-normal">
				Programmierkurse für alle
			</h1>
			<p class="text-2xl text-white p-4">Praxisorientiert, projektbasiert, leicht zu verstehen</p>
			<a href="/youtube" class="btn mt-4 bg-blue-400 uppercase px-12 hover:bg-blue-700"
				>Starte noch heute</a
			>
		</div>
		<div class="md:mt-40 px-4 py-10 rounded-lg bg-blue-400 flex flex-col m-4 md:flex-row">
			<div class="logo flex-1">
				<img src="/images/ytaccount.png" alt="" />
			</div>
			<div class="links flex-1 p-4 text-white text-center">
				<div class="content">
					<h1 class="text-3xl uppercase font-extrabold pb-4">Coding Crashkurse auf YouTube</h1>
					<p class="pb-4 text-xl">
						200+ kostenlose Tutorials und Crashkurse zu vielen unterschiedlichen Themen
					</p>
				</div>

				<div class="flex flex-col justify-center my-8 md:flex-row">
					<a
						href="https://www.youtube.com/channel/UCikLKUS0DZWMkukbkYDG49Q" target="_blank" rel="noreferrer"
						class="btn mr-2 mb-2 px-8 bg-black border-1 border-white hover:bg-blue-700"
						>Direkt auf YouTube</a
					>
					<a
						href="/kurse"
						class="btn mr-2 bg-blue-700 px-8 border-1 border-white hover:bg-blue-700"
						>Meine Videos</a
					>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	.wrapper {
		background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
			url('/images/programming.jpg') no-repeat center center fixed;
		-webkit-background-size: cover;
		-moz-background-size: cover;
		-o-background-size: cover;
		background-size: cover;
		min-height: calc(100vh - 40px);
	}

	@media only screen and (max-width: 767px) {
		.wrapper {
			min-height: 1000px;
		}
	}
</style>
