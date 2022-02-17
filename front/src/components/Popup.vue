<template>
  <div class="popup" :class="{'fixed-to-top': showPopupNo === 3}">
    <div class="popup-content" v-if="showPopupNo === 1">
      <h1>Pomagaj graditi stanovanjsko skupnost.</h1>
      <h3>Izberi, kar si želiš.</h3>
      <ObjectOptions
          @choose-object="objectIsChosen"
      />
    </div>
    <div class="popup-content" v-if="showPopupNo === 2">
      <h1>Pomagaj graditi stanovanjsko skupnost.</h1>
      <h3>Izberi gradnik.</h3>
      <ObjectVariations
          :variations="objectChosen"
          @choose-variation="variationIsChosen"
      />
      <p @click="backToObject" class="back-button">&lt; Nazaj</p>
    </div>
    <div class="popup-content" v-if="showPopupNo === 3">
      <h1>Pomagaj graditi stanovanjsko skupnost.</h1>
      <h3>Izberi prazen prostor na zemljevidu.</h3>
      <div class="object-panel-chosen">
        <div class="object-option">
          <div class="object-img">
            <img :src="require('../assets/tiles/' + objectVariationChosen + '.png')" />
          </div>
        </div>
      </div>
      <p @click="backToVariation" class="back-button">&lt; Nazaj</p>
    </div>
    <div class="popup-content add-message" v-if="showPopupNo === 4">
      <h3>Dodaj sporočilo</h3>
      <p>Tvoje ime ne bo objavljeno.</p>
      <form id="submit-message">
        <textarea v-model="messageText" rows="10" />
        <p v-if="messageError" class="message-error">Vsebina sporočila ne more biti prazna</p>
        <div>
          <button type="button" @click="saveMessage" :disabled="buttonText !== 'Oddaj'">{{ buttonText }}</button>
          <span @click="thankyou">Preskoči</span>
        </div>
      </form>
    </div>
    <div class="popup-content thank-you-message" v-if="showPopupNo === 5">
      <h1>Povej naprej!</h1>
      <p>Več nas bo gradilo, prej bodo stanovanjske zadruge zaživele tudi pri nas.</p>
      <h3>Skopiraj povezavo</h3>
      <span @click="copyLink">{{ shareUrl }}</span>
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
      objectChosen: '',
      tilePlaced: false,
      messageText: '',
      messageError: false,
      shareUrl: 'djnd.si/anhk1790', // to do: change url to landing page
      buttonText: 'Oddaj'
    }
  },
  watch: {
  },
  props: {
    apiUrl: {
      type: String,
      default: ''
    },
    token: {
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
    objectVariationChosen: {
      type: Number,
      default: null
    },
    showPopupNo: {
      type: Number,
      default: 1
    }
  },
  methods: {
    objectIsChosen(n) {
      this.objectChosen = n
      this.$emit('object-chosen');
    },
    variationIsChosen(i) {
      this.$emit('variation-chosen', i);
    },
    async saveMessage() {
      if (!this.messageText) {
        this.messageError = true
      }
      if (this.tileChosenId && this.messageText) {
        this.buttonText = "PoŠiljam..."
        this.messageError = false
        await this.axios.post(this.apiUrl + '/api/message/', {
          'index': this.tileChosenId,
          'text': this.messageText,
          'token': this.token
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
      this.$emit('thank-you');
    },
    copyLink(e) {
      const el = e.target;
      const sel = window.getSelection();
      if (sel.toString() === ''){ // no text selection
        window.setTimeout(function(){
          const range = document.createRange(); // range object
          range.selectNodeContents(el); // sets Range
          sel.removeAllRanges(); // remove all ranges from selection
          sel.addRange(range);// add Range to a Selection.
        },1);
      }
    },
    backToObject() {
      this.$emit('back-to-object');
    },
    backToVariation() {
      this.$emit('back-to-variation');
    }
  }
}
</script>

<style>
.popup {
  position: fixed;
  z-index: 1000;
  background-image: url("../assets/popup-blob.png");
  background-size: 100% 100%;;
  top: 10vh;
  left: 5vw;
  height: auto;
  width: 80vw;
  max-width: 361px;
  padding: 20px;
}

.popup.fixed-to-top {
  top: 10px;
}

@media (min-width: 992px) {
  .popup, .popup.fixed-to-top {
    top: 50vh;
    left: 50px;
    transform: translateY(-50%);
  }
}

.popup-content {
  margin: 32px;
}

@media (min-width: 992px) {
  .popup-content {
    margin: 40px;
  }
}

h1 {
  font-family: 'Azeret Mono', monospace;
  font-size: 1.25rem;
}
h3 {
  font-family: 'Azeret Mono', monospace;
  font-weight: 400;
  font-size: 1rem;
}
@media (min-width: 992px) {
  h1 {
    font-size: 1.5rem;
  }
  h3 {
    font-size: 1rem;
  }
}

.object-option {
  display: inline-block;
  padding-right: 16px;
  width: 62px;
}
.object-option:nth-child(3n+3) {
  padding-right: 0;
}
.object-option:hover {
  cursor: pointer;
}

.object-panel-chosen {
  display: none;
}

@media (min-width: 992px) {
  .object-panel-chosen {
    display: flex;
    justify-content: center;
    margin-top: 32px;
    margin-bottom: 32px;
  }

  .object-panel-chosen .object-option {
    padding-right: 0;
  }
}

.object-option:hover .object-img {
  outline: 2px solid black;
}
.object-option span {
  font-family: 'Quicksand', sans-serif;
  font-weight: 600;
  font-size: 12px;
  text-align: center;
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
}


.object-img {
  padding: 10px;
  border: 2px solid #000000;
}
.object-img img {
  display: block;
  height: 40px;
  width: 40px;
}

.popup-content .back-button {
  font-family: 'Azeret Mono', monospace;
  cursor: pointer;
}
@media (min-width: 992px) {
  .object-option {
    padding-right: 14px;
    width: 72px;
  }
  .object-img img {
    display: block;
    height: 48px;
    width: 48px;
  }

}
.popup-content form textarea {
  width: calc(100% - 40px);
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
  color: #82CEE8;
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

.popup-content form .message-error {
  color: red;
}

.popup-content form button:hover {
  background-color: #82CEE8;
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
</style>
