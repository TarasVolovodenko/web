<template>
<div class="carousel">
    <agile class="main" ref="main" :options="options1" :as-nav-for="asNavFor1">
        <div class="slide" v-for="(slide, index) in slides" :key="index" :class="`slide--${index}`"><img :src="slide.image" :alt="slide.alt" /></div>
    </agile>
    <agile class="thumbnails" ref="thumbnails" :options="options2" :as-nav-for="asNavFor2">
        <div class="slide slide--thumbniail" v-for="(slide, index) in slides" :key="index" :class="`slide--${index}`" @click="$refs.thumbnails.goTo(index)"><img :src="slide.image" :alt="slide.alt" /></div>
    </agile>
</div>
</template>

<script>
import {
    VueAgile
} from 'vue-agile'

export default {
    components: {
        agile: VueAgile,
    },
    data() {
        return {
            asNavFor1: [],
            asNavFor2: [],
            options1: {
                dots: false,
                fade: true,
                navButtons: false
            },

            options2: {
                autoplay: true,
                centerMode: false,
                dots: false,
                navButtons: false,
                slidesToShow: 3,
                infinite: true,
                initialSlide: 0,
                responsive: [{
                    breakpoint: 900,
                    settings: {
                        slidesToShow: 4,
                    }
                }]
            },

            slides: [{
                    image: require("@/../images/Rectangle_19.jpg"),
                    alt: "pollution image"
                },
                {
                    image: require("@/../images/Rectangle_29.jpg"),
                    alt: "pollution image"
                },
                {
                    image: require("@/../images/Rectangle_30.jpg"),
                    alt: "pollution image"
                },
                {
                    image: require("@/../images/Rectangle_31.jpg"),
                    alt: "pollution image"
                }
            ]
        }
    },
    mounted() {
        this.asNavFor1.push(this.$refs.thumbnails)
        this.asNavFor2.push(this.$refs.main)
    },
}
</script> 

<style lang="scss">
// Slides styles
.main {
    margin-bottom: 1vw;

}

.slide {
    align-items: center;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    padding: 0 0.5vw;
}

.slide--thumbniail {
    cursor: pointer;
    height: 105px;
    padding: 0 0.5vw;
    transition: opacity .3s;
    display: flex;
    justify-content: flex-start;
}

.slide--thumbniail:hover {
    opacity: .75;
}

.slide img {
    width: 100%;
    object-fit: cover;
    object-position: center;
}
</style>
