<script lang="ts">
    import { onMount, onDestroy } from 'svelte';

    export let video_id: string;
    export let link: string;
    export let title: string;
    export let active_promotion: boolean = false;
    export let promo_until: string = '';

    let countdown = '';
    let promotion_active = active_promotion;

    function updateCountdown() {
        const now = new Date().getTime();
        const promoEndTime = new Date(promo_until).getTime();
        const distance = promoEndTime - now;

        if (distance > 0) {
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            countdown = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        } else {
            promotion_active = false;
            clearInterval(interval);
        }
    }

    let interval: number;
    onMount(() => {
        if (active_promotion) {
            updateCountdown();
            interval = window.setInterval(updateCountdown, 1000);
        }
    });

    // Cleanup interval on component destroy
    onDestroy(() => {
        if (interval) {
            clearInterval(interval);
        }
    });
</script>

<a target="_blank" rel="noreferrer" href={link}>
    <div class="card w-full bg-base-100 shadow-xl relative">
        <figure><img src={video_id} alt="Thumbnail" /></figure>
        <div class="card-body text md:h-80">
            <h3 class="card-title pt-4 pb-10">{title}</h3>
            <slot name="description" />
        </div>
        {#if promotion_active}
            <div class="countdown-timer absolute top-0 left-0 w-full p-2 bg-red-600 text-white text-sm text-center">
                Best Price Course for $9.99 - {countdown}
            </div>
        {/if}
    </div>
</a>

<style>
    .countdown-timer {
        border-radius: 0 0 8px 8px;
    }
</style>
