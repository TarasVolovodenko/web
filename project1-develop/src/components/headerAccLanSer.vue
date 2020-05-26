<template>
<div class="hals">
  <div class="hals__flex">
      <LanguageSwicher
            :selected="selected.languages"
            :items="languages"
            :select="select('languages')"
      />
      <svg class="hals__svg" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M8 8C6.88954 8 5.9433 7.61014 5.16129 6.83041C4.37928 6.05068 3.98827 5.10721 3.98827 4C3.98827 2.89279 4.37928 1.94932 5.16129 1.16959C5.9433 0.389864 6.88954 0 8 0C9.11046 0 10.0567 0.389864 10.8387 1.16959C11.6207 1.94932 12.0117 2.89279 12.0117 4C12.0117 5.10721 11.6207 6.05068 10.8387 6.83041C10.0567 7.61014 9.11046 8 8 8ZM8 10.0117C8.98534 10.0117 10.0723 10.152 11.261 10.4327C12.4497 10.7135 13.5367 11.1735 14.522 11.8129C15.5073 12.4522 16 13.1774 16 13.9883V16H0V13.9883C0 13.1774 0.492669 12.4522 1.47801 11.8129C2.46334 11.1735 3.55034 10.7135 4.739 10.4327C5.92766 10.152 7.01466 10.0117 8 10.0117Z" fill="#F2F2F2"/>
    </svg>
    </div>
  <SearchBar/>
</div>
</template>

<script>
import SearchBar from '@/components/headerComponents/searchBar'
import LanguageSwicher from '@/components/headerComponents/languageSwicher'
export default {
  name: 'HeaderAccLanSer',
  components: {
    SearchBar,
    LanguageSwicher
  },
  data () {
    return {
      selected: {
        languages: 1
      }
    }
  },
  props: {
    languages: Array
  },
  methods: {
    select (key) {
      return (id) => {
        this.selected[key] = id
      }
    },
    selectDefault: () => {
      Object.keys(this.selected).map(key => this.select(key)(0))
    }
  }
}
</script>
<style lang="scss">
.hals {
  @include FCenter(space-around);
  width: rem(125);
  &__flex {
    @include FCenter(space-between);
    width: rem(80);
  }
  &__block {
    width: rem(50);
    position: relative;
  }
  &__block:after {
    top: 50%;
    left: 70%;
    margin-top: rem(-2);
    position: absolute;
    cursor: pointer;
    pointer-events: none;
    content: "";
    width: 0;
    height: 0;
    display: block;
    border-style: solid;
    border-width: 5px 5px 0 5px;
    border-color: $white transparent transparent transparent;
  }
  &__select {
    cursor: pointer;
    width: 100%;
    outline: none;
    color: $white;
    font-size: rem(20);
    background: none;
    border: none;
    appearance: none;
  }
  svg path {
  fill:inherit;
  stroke:inherit;
  stroke-width:inherit;
  }
  &__svg {
    fill: $white;
    transition-duration: .5s;
  }
  &__svg:hover {
    cursor: pointer;
    fill: $red;
  }
}
</style>
