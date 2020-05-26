<template>
  <div class="HomeHeader">
    <Navbar/>
    <div class="site-logo-slogan">
      <div class="main-logo">
        <a href="." class="site-logo icon"></a>
        <a href="." class="site-name">ECOMAP</a>
      </div>
      <p>Be better. Live better. Save Earth</p>
    </div>
    <a class="arrow-icon" href="#home-content"></a>
  </div>
</template>

<script>
import Navbar from '@/components/navbar.vue'
export default {
  name: 'HomeHeader',
  components: {
    Navbar
  }
}
</script>
<style lang="scss">
.HomeHeader {
  min-height: 600px;
  background-image: linear-gradient(180deg, rgba(255, 255, 255, 0) 0%, rgba(32, 31, 48, 0.35) 59.38%, #201F30 100%), url(../resources/home-bg.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position-y: 50%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-content: center;
}
.site-logo-slogan {
  text-align: center;
  display: flex;
  flex-direction: column;
}
.site-logo-slogan .site-name {
  font-size: 96px;
  height: 100%;
  padding: 0;
}
.site-logo-slogan #site-logo {
  width: 70px;
  height: 70px;
  margin: 0 10px 0 0;
  align-self:center;
}
.site-logo-slogan p {
  font-size: 34px;
}
.main-logo {
  display: flex;
  justify-content: center;
  align-items: center;
}
.main-logo .site-logo {
  width: 75px;
  height: 75px;
  margin: 0;
}
.arrow-icon {
  width: 50px;
  height: 30px;
  background-image: url(../resources/down-arrow.svg);
  background-repeat: no-repeat;
  background-size: cover;
  cursor: pointer;
  margin: 30px auto 40px auto;
}
</style>
