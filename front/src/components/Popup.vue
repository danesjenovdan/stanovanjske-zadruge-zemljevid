<template>
  <div class="popup">
    <div class="popup-content" v-if="!tileChosen && !tilePlaced">
      <h1>Pomagaj graditi virtualno skupnost.</h1>
      <h3>Izberi prazno območje.</h3>
    </div>
    <div class="popup-content" v-if="!tilePlaced">
      <h3 v-if="tileChosen && !objectChosen">Izberi objekt</h3>
      <h3 v-if="objectChosen">Izberi variacijo</h3>
      <ObjectOptions
          v-if="tileChosen && !objectChosen"
          @choose-option="showVariations"
      />
      <ObjectVariations
          v-if="objectChosen"
          :variations="objectVariations"
          @place-on-map="placeOnMap"
      />
    </div>
    <div class="popup-content add-message" v-if="tilePlaced && !showThankYou">
      <h3>Dodaj sporočilo</h3>
      <p>Tvoje ime ne bo objavljeno.</p>
      <form id="submit-message">
        <textarea v-model="messageText" rows="10" />
        <div>
          <button type="button" @click="saveMessage" :disabled="buttonText !== 'Oddaj'">{{ buttonText }}</button>
          <span @click="thankyou">Preskoči</span>
        </div>
      </form>
    </div>
    <div class="popup-content thank-you-message" v-if="showThankYou">
      <h1>Povej naprej</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      <h3>Skopiraj povezavo</h3>
      <span :class="{ 'copied': copiedUrl }" @click="copyLink">{{ shareUrl }}</span>
    </div>
  </div>
</template>

<script>
import ObjectOptions from "./ObjectOptions";
import ObjectVariations from "./ObjectVariations";

export default {
  name: "Popup",
  components: {ObjectVariations, ObjectOptions},
  data() {
    return {
      objectChosen: false,
      objectVariations: 0,
      tilePlaced: false,
      messageText: "",
      showThankYou: false,
      shareUrl: "djnd.si/anhk1790",
      copiedUrl: false,
      buttonText: "Oddaj"
    }
  },
  props: {
    apiUrl: {
      type: String,
      default: ''
    },
    tileChosen: {
      type: Boolean,
      default: false
    },
    tileChosenId: {
      type: Number,
      default: null
    },
  },
  methods: {
    showVariations(n) {
      this.objectChosen = true
      this.objectVariations = n
    },
    placeOnMap(i) {
      this.$emit('place-on-map', i);
      this.tilePlaced = true;
    },
    async saveMessage() {
      if (this.tileChosenId) {
        this.buttonText = "PoŠiljam..."
        await this.axios.post(this.apiUrl + '/api/message/', {
          "index": this.tileChosenId,
          "text": this.messageText
        }).then((res) => {
          if (res.status === 200) {
            this.thankyou()
            this.$emit('new-message', {
              "index": this.tileChosenId,
              "text": this.messageText
            });
          } else {
            alert("Nekaj je šlo narobe :(")
          }
        })
      }
    },
    thankyou() {
      this.showThankYou = true;
    },
    copyLink() {
      navigator.clipboard.writeText(this.shareUrl);
      this.copiedUrl = true
    }
  }
}
</script>

<style>
.popup {
  position: fixed;
  z-index: 1000;
  background-image: url("../assets/popup-blob.png");
  top: 300px;
  left: 50px;
  height: 354px;
  width: 361px;
  padding: 40px;

}
@media (min-width: 992px) {
  .popup {
    top: 50vh;
    left: 50px;
    transform: translateY(-50%);
  }
}
.popup-content {
  margin: 40px;
}

h1 {
  font-family: 'Azeret Mono', monospace;
}
h3 {
  font-family: 'Azeret Mono', monospace;
  font-weight: 400;
}
.object-option {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  margin: 10px;
}
.object-option:hover {
  cursor: pointer;
}
.object-option:hover .object-img {
  outline: 2px solid black;
}
.object-option span {
  font-family: 'Quicksand', sans-serif;
  font-weight: 600;
  margin-top: 5px;
}
.object-img {
  padding: 10px;
  border: 2px solid #000000;
}
.object-img img {
  display: block;
  height: 48px;
  width: 48px;
}
.popup-content form textarea {
  width: 100%;
  border: 2px solid #000000;
  margin-bottom: 1rem;
  padding: 1rem;
}

.popup-content form div {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.popup-content form div span {
  font-family: 'Quicksand', sans-serif;
  font-size: 0.875rem;
  text-decoration: underline;
  cursor: pointer;
}

.popup-content form div span:hover {
  color: #4d957f;
}

.popup-content form button {
  color: black;
  font-family: 'Quicksand', sans-serif;
  font-weight: 600;
  font-size: 1rem;
  background-color: white;
  background-image: url('../assets/button-border.png');
  background-repeat: no-repeat;
  background-size: 100% 100%;
  border: none;
  padding: 0.5rem 2rem;
  cursor: pointer;
}
.popup-content form button:hover {
  background-color: #4d957f;
}
.popup-content.add-message h3 {
  margin: 0;
}
.popup-content.add-message p {
  margin-top: 0;
  font-family: 'Quicksand', sans-serif;
}
.popup-content.thank-you-message h1 {
  margin-bottom: 0.5rem;
}
.popup-content.thank-you-message p {
  margin-top: 0;
  font-family: 'Quicksand', sans-serif;
}
.popup-content.thank-you-message h3 {
  margin-top: 1.5rem;
  margin-bottom: 1rem;
}
.popup-content.thank-you-message span {
  display: block;
  font-family: 'Azeret Mono', monospace;
  font-style: italic;
  border: 2px solid #000000;
  padding: 10px 40px;
  cursor: pointer;
}
.popup-content.thank-you-message span.copied {
  background-color: lightblue;
}
</style>
