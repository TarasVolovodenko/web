<template>
<div class="wrapper donatepage">
  <DonateHeader/>
  <DonateContent/>
  <Footer/>
</div>
</template>

<script>
import DonateHeader from '@/layout/donate-header'
import DonateContent from '@/layout/donate-content'
import Footer from '@/layout/footertd'
export default {
  name: 'DonatePage',
  components: {
    DonateHeader,
    DonateContent,
    Footer
  }
}
</script>

<style lang="scss">
</style>
