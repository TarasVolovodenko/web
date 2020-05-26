<template>
    <input type="text" value = {} class="textfield">
</template>

<script>
export default {
  name: 'TextField',
  data () {
    return {
    }
  },
  props: [
  ],
  methods: {
  }
}
</script>

<style lang="scss">
.textfield {
    font-size: 20px;
    padding: 8px;
    border-style: hidden hidden solid hidden;
    border-color: $dark-color;
    border-width: 2px;
    margin: 5px 0px;
    outline: none;
}
</style>
