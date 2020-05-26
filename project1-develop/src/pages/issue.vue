<template>
<div class="wrapper issue">
    <Header />
    <Content />
    <Footer />
    <!-- <Modal/> -->
</div>
</template>

<script>
import Header from '@/layout/header'
import Content from '@/layout/issue_content'
import Footer from '@/layout/footer'
// import Modal from '@/components/modal'
export default {
    name: 'issue',
    components: {
        Header,
        Content,
        Footer
        // Modal
    }
}
</script>

<style lang="scss">
.wrapper {
    min-width: 100%;

}

;

::-webkit-scrollbar {
    width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
    background: transparent;
}

/* Handle */
::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
    background: #555;
}
</style>
