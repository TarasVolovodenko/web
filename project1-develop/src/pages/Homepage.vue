<template>
<div class="wrapper homepage">
  <HomeHeader/>
  <HomeContent/>
  <Footer/>
</div>
</template>

<script>
import HomeHeader from '@/layout/home-headertd'
import HomeContent from '@/layout/home-content'
import Footer from '@/layout/footertd'
export default {
  name: 'HomePage',
  components: {
    HomeHeader,
    HomeContent,
    Footer
  }
}
</script>

<style lang="scss">
</style>
