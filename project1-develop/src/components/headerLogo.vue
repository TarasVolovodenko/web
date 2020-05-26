<template>
  <div class="headerLogo">
    <svg  class="headerLogo__svg"  viewBox="0 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path class="headerLogo__path" d="M3.20331 6.33033C1.15767 8.37704 0.00587913 11.1511 2.24442e-05 14.0453C-0.00583424 16.9396 1.13472 19.7182 3.17206 21.7732C5.46891 16.4589 9.56263 12.0198 14.672 9.37827C10.2619 13.1111 7.28502 18.2604 6.25016 23.9458C10.3126 25.8684 15.3126 25.165 18.6719 21.8045C24.1094 16.3651 25 0 25 0C25 0 8.64076 0.890936 3.20331 6.33033Z"/>
    </svg>
    <div class="headerLogo__name">ecomap</div>
  </div>
</template>

<script>
export default {
  name: 'HeaderLogo'
}
</script>
<style lang="scss">
.headerLogo {
  transition-duration: .5s;
  @include FCenter(space-between);
  &__name {
    margin-left: rem(6);
    font-size: rem(24);
    color: $white;
    text-transform: uppercase;
    transition-duration: .5s;
  }
  svg path {
  fill:inherit;
  stroke:inherit;
  stroke-width:inherit;
  }
  &__svg {
    fill: $white;
    transition-duration: .5s;
    width: 25px;
    height: 25px;
  }
}
.headerLogo:hover {
  cursor: pointer;
}

.headerLogo:hover .headerLogo__svg {
  transform: rotate(360deg);
  fill: $red;
}
.headerLogo:hover .headerLogo__name {
  color: $red;
}
</style>
