<template>
    <div class="Slider">
        <div class="slider-title">
            <h1>{{slider_title}}</h1>
        </div>
        <div class="slides">
            <div v-for="n in 5" v-bind:key="n" :id="'slide-' + slider_title + '-' + n">
                <div class="image" v-bind:style="{backgroundImage: 'url(' + image_urls[n - 1] +')'}"/>
                    <div class="text-block">
                    <h2>{{titles[n - 1]}}</h2>
                    <p>{{descriptions[n - 1]}}</p>
                    <a class="read-more" :href="urls[n - 1]"><h3>Read more</h3><div class="right-arrow-icon"/></a>
                </div>
            </div>
        </div>
        <div class="slider-buttons">
            <a v-for="n in 5" v-bind:key="n" :href="'#slide-' + slider_title + '-' + n" class="slider-btn" :class="{sliderhighlight:highlighted == n}" @click="highlighted = n"/>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Slider',
  props: {
    slider_title: String,
    image_urls: Array,
    urls: Array,
    titles: Array,
    descriptions: Array
  },
  data () {
    return {
      highlighted: 1
    }
  }
}
</script>

<style lang="scss">
.Slider {
  display: flex;
  width: 100%;
  padding: 100px 40px;
  box-sizing: border-box;
}
.Slider .image {
  width: 650px;
  height: 360px;
  background-position: center;
  background-size: cover;
  margin: 0;
}
.slider-title {
  height: 360px;
  width: 150px;
  text-align: center;
  writing-mode: vertical-rl;
}
.slider-title h1 {
  transform: rotate(180deg);
  font-size: 140px;
  width: 100%;
}
.slides, .slides>* {
  width: 100%;
  height: 360px;
}
.slides > * {
  display: flex;
}
.text-block {
  display: flex;
  flex-direction: column;
  margin-left: 40px;
  margin-right: auto;
  width: 40%;
}
.text-block>h2 {
  text-align: left;
  margin-bottom: 25px;
}
.text-block>p {
  margin-bottom: 25px;
}
.text-block>a {
    color: $white;
    text-decoration: none;
}
.slides {
  overflow: hidden;
  transition-property: overflow;
  transition: 0.5s;
  scroll-behavior: smooth;
}
.slider-buttons {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 360px;
  min-width: 12px;
}
.slider-btn {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin: 8px 0;
  background-color: $white;
}
.sliderhighlight, .slider-btn:hover {
  width: 12px;
  height: 12px;
  margin-top: 6px;
  margin-bottom: 6px;
}
.right-arrow-icon {
  background-image: url('../resources/right-arrow.svg');
  width: 12px;
  height: 18px;
  background-size: cover;
  margin-left: 10px;
}
.read-more {
  display: flex;
  align-items: center;
  margin-right: auto;
}
</style>
