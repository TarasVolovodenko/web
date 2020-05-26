<template>
<button type="button" @click="handleClick" class="btn btn-outline-light">
    <span>{{name}}</span>
</button>
</template>

<script>
export default {
  name: 'CustomButton',
  data () {
    return {
      bname: ''
    }
  },
  props: [
    'name'
  ],
  methods: {
    handleClick () {
      this.$emit('click')
    }
  }
}
</script>

<style lang="scss">
.btn {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0px;
    border: 1px solid white;
    box-sizing: border-box;
    width: 300px;
    height: 60px;
    background-color: transparent;
    outline: none;
    transition: 0.5s;
    cursor: pointer;
    //$btn-border-radius-base:0!important;
}
.btn:hover span {
    color: $bcolor;
}
.btn:hover {
    background-color: $fcolor;
}
.btn span {
    color: $fcolor;
    padding: 0px;
    font-size: $accent-fsize;
    // line-height: $accent-fline-hight;
}
@media only screen and (max-width: 1150px) {
    .btn span {
        font-size: calc(#{$accent-fsize} - 9px);
    }
    .btn {
        border: 1px solid white;
        width: 200px;
        height: 50px;
        //$btn-border-radius-base:0!important;
    }
}
@media only screen and (max-width: 910px) {
    .btn {
        border: 1px solid white;
        width: 200px;
        height: 50px;
        //$btn-border-radius-base:0!important;
    }
}
</style>