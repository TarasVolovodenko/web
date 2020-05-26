<template>
<div class="wrapper contactpage">
  <Header/>
  <ContactsContent/>
  <Footer/>
  <!-- <Modal/> -->
</div>
</template>

<script>
import Header from '@/layout/headertd'
import ContactsContent from '@/layout/contacts-content'
import Footer from '@/layout/footertd'
// import Modal from '@/components/modal'
export default {
  name: 'ContactsPage',
  components: {
    Header,
    ContactsContent,
    Footer
    // Modal
  }

}
</script>

<style lang="scss">
</style>
