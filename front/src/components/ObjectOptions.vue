<template>
  <div>
    <div>
      <div class="object-option" @click="showVariations(1)">
        <div class="object-img">
          <img src="@/assets/tiles/11.png" />
        </div>
        <span>Hiša</span>
      </div>
      <div class="object-option" @click="showVariations(2)">
        <div class="object-img">
          <img src="@/assets/tiles/21.png" />
        </div>
        <span>Blok</span>
      </div>
      <div class="object-option" @click="showVariations(3)">
        <div class="object-img">
          <img src="@/assets/tiles/30.png" />
        </div>
        <span>Zelenje</span>
      </div>
    </div>
    <div>
      <div class="object-option" @click="showVariations(4)">
        <div class="object-img">
          <img src="@/assets/tiles/45.png" />
        </div>
        <span>Hobi</span>
      </div>
      <div class="object-option" @click="showVariations(5)">
        <div class="object-img">
          <img src="@/assets/tiles/54.png" />
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
