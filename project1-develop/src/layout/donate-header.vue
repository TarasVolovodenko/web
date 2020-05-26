<template>
  <div class="DonateHeader">
    <Navbar/>
    <h2>Donate</h2>
    <a class="arrow-icon" href="#donate-info"></a>
  </div>
</template>

<script>
import Navbar from '@/components/navbar.vue'
export default {
  name: 'DonateHeader',
  components: {
    Navbar
  }
}
</script>
<style lang="scss">
.DonateHeader {
  height: 400px;
  background-image: linear-gradient(180deg, rgba(255, 255, 255, 0) 0%, rgba(32, 31, 48, 0.35) 59.38%, #201F30 100%), url(../resources/donate-bg.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position-y: 50%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-content: center;
}
.DonateHeader h2 {
  margin: auto;
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
