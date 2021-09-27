<template>
  <div>
    <div>
      <div class="object-option" @click="showVariations('domovanje')">
        <div class="object-img">
          <img src="@/assets/tiles/20.png" />
        </div>
        <span>Domovanje</span>
      </div>
      <div class="object-option" @click="showVariations('skupnost')">
        <div class="object-img">
          <img src="@/assets/tiles/23.png" />
        </div>
        <span>Skupnost</span>
      </div>
      <div class="object-option" @click="showVariations('park')">
        <div class="object-img">
          <img src="@/assets/tiles/30.png" />
        </div>
        <span>Park</span>
      </div>
    </div>
    <div>
      <div class="object-option" @click="showVariations('pokrajina')">
        <div class="object-img">
          <img src="@/assets/tiles/50.png" />
        </div>
        <span>Pokrajina</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ObjectOptions",
  methods: {
    showVariations(n) {
      this.$emit('choose-object', n);
    }
  }
}
</script>

<style scoped>

</style>
