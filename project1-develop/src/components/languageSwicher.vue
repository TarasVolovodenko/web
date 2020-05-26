<template>
  <div class="LanguageSwicher">
    <div tabindex="0" class="LanguageSwicher__selected" @click="clicked()">{{selectedItem().name}}</div>
    <transition name="fade">
    <span class="LanguageSwicher__box" v-if="show">
      <p class="LanguageSwicher__option" v-for="({id, name}, i) in unselectedItems()" :key="i" @click="selectItem(id)">{{name}}</p>
    </span>
  </transition>
  </div>
</template>
<script>
export default {
  name: 'LanguageSwicher',
  data () {
    return {
      show: false
    }
  },
  props: {
    selected: Number,
    items: Array,
    select: Function
  },
  methods: {
    clicked () {
      this.show = !this.show
    },
    hide () {
      this.show = false
    },
    selectItem (id) {
      this.select(id)
      this.show = false
    },
    selectedItem () {
      return this.items.find(item => item.id === this.selected) || this.items[0]
    },
    unselectedItems () {
      return this.items.filter(item => item.id !== this.selected)
    }
  },
  mounted () {
    this.selectedItemId = this.defaultItem
    this.clicked = this.clicked.bind(this)
    this.hide = this.hide.bind(this)
    this.selectItem = this.selectItem.bind(this)
    this.selectedItem = this.selectedItem.bind(this)
    this.unselectedItems = this.unselectedItems.bind(this)
    document.addEventListener('click', this.hide, true)
  },
  beforeDestroy () {
    document.removeEventListener('click', this.hide)
  }
}
</script>
<style lang="scss">
.LanguageSwicher {
  font-size: rem(20);
  width: rem(45);
  position: relative;
  &__selected {
    position: relative;
    padding: 5px;
    border: none;
    background: transparent;
    font-size: rem(20);
    color: $white;
    text-overflow: ellipsis;
    transition: color .5s;
  }
  &__selected:after {
    position: absolute;
    content: "";
    top: 40%;
    left: 90%;
    width: 5px;
    height: 5px;
    border-top: 2px solid $white;
    border-left: 2px solid $white;
    transform: rotate(45deg);
    transition-duration: .5s;
  }
  &__selected:focus {
    outline: none;
  }
  &__selected:focus:after {
    transform: rotate(225deg);
  }
  &__selected:hover {
    cursor: pointer;
  }
  &__box {
    width: rem(45); // or 100%
    cursor: pointer;
    display: block;
    position: absolute;
    color: $white;
    border: 1px solid $white;
  }
  &__option {
    padding: 5px;
    transition-duration: .5s;
  }
  &__option:not(:first-child) {
    border-top: 1px solid $white;
  }
  // &__option:first-child {
  //   border-top: none;
  //   border-radius: 0 5px 0 0;
  // }
  // &__option:last-child {
  //   border-radius: 0 0 5px 0;
  // }
  &__option:hover {
    background-color: $gray;
    color: $dark;
  }
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
  transition: margin-top .5s;
}
.fade-enter, .fade-leave-to  {
  opacity: 0;
  margin-top: -10px;
}
</style>
