<template>
  <nav class="headerMenu">
    <router-link class="headerMenu__link" tag="li" v-for="item in navbars" :key="item.id" :to="{path:item.router}">{{item.names}}</router-link>
  </nav>
</template>

<script>
export default {
  name: 'HeaderMenu',
  data () {
    return {
      navbars: [
        { names: 'Home', router: '/xx' },
        { names: 'Issues', router: '/xx' },
        { names: 'Fixed', router: '/Fixed' },
        { names: 'Events', router: '/Event' },
        { names: 'Donate', router: '/xx' },
        { names: 'Contacts', router: '/xx' }
      ]
    }
  }
}
</script>
<style lang="scss">
.headerMenu {
  color: $white;
  width: rem(650);
  @include FCenter(space-between);
  &__link {
    font-size: rem(20);
    position: relative;
  }
  &__link:after{
    @include After(2px, $white, -2);
  }
  &__link:hover {
    cursor: pointer;
  }
  &__link:hover, &__link:focus  {
    &:after {
      width: 100%;
    }
  }
}
</style>
