<template>
  <v-container>
      <v-layout wrap>
        <v-flex sm12 md6 offset-md3>
          <v-card elevation="4" light tag="section">
            <v-card-title>
              <v-layout align-center justify-start>
                <h3>
                  {{ platformName }}
                </h3>
              </v-layout>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
              <p>Enter the lead data:</p>
              <v-form>  
                <v-text-field v-model="scoreSelect" single-line type="number" :rules="[v => !!v || 'Score is required']" label="Lead Score" outlined required/>
                <v-text-field v-model="ageSelect" single-line type="number" :rules="[v => !!v || 'Age is required']" label="Age" outlined required/>
                <v-select v-model="genderSelect" :items="genderItems" :rules="[v => !!v || 'Gender is required']" label="Gender" outlined required></v-select>
                <v-select v-model="countrySelect" :items="countryItems" :rules="[v => !!v || 'Country is required']" label="Country" outlined required></v-select>
                <v-select v-model="ethnSelect" :items="ethnItems" :rules="[v => !!v || 'Ethnicity is required']" label="Ethnicity" outlined required></v-select>
                <v-text-field v-model="sizeSelect" single-line type="number" :rules="[v => !!v || 'Company Size is required']" label="Company Size" outlined required/>
                <v-select v-model="industrySelect" :items="industryItems" :rules="[v => !!v || 'Industry is required']" label="Industry" outlined required></v-select>
              </v-form>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions :class="{ 'pa-3': $vuetify.breakpoint.smAndUp }">
              <v-btn color="error" text @click="clear()">
                Clear
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn v-if="isSetup" color="info" :large="$vuetify.breakpoint.smAndUp" @click="classify()">
                <v-icon left>mdi-cloud-upload</v-icon> Predict
              </v-btn>
              <v-btn v-else color="info" :large="$vuetify.breakpoint.smAndUp" disabled>
                Please wait...
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
        <v-flex sm12 md6 offset-md3>
          <v-layout align-center justify-space-between>
            <p class="caption my-3">
              <a href="#">Privacy Policy</a>
              |
              <a href="#">Terms of Service</a>
            </p>
            <p class="caption my-3">Powered by <a href="#">ml5.js</a></p>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
  export default {
    name: 'MLMain',
    data: () => ({
      isSetup: false,
      salesreps: ['Elliot', 'Stacy', 'Andre', 'Frank'],
      neuralNetwork: null,
      ranking: [],
      platformName: 'BIS3060',
      scoreSelect: 69,
      ageSelect: 46,
      genderSelect: 'female',
      genderItems: ['male', 'female'],
      countrySelect: 'France',
      countryItems: ['Germany', 'France', 'England', 'Poland'],
      ethnSelect: 'French',
      ethnItems: ['German', 'French', 'English', 'Polish'],
      sizeSelect: 49,
      industrySelect: 'Retail', 
      industryItems: ['Software', 'Retail', 'Marketing'],

    }),
    computed: {
    },
    methods: {
      predict() {
        console.log('Predicting results...'); 
      },
      clear() {
        //this.$v.$reset()
        console.log('Clearing input...'); 
        this.scoreSelect = null; 
        this.ageSelect = null; 
        this.genderSelect = null;
        this.countrySelect = null; 
        this.ethnSelect = null; 
        this.sizeSelect = null;
        this.industrySelect = null;
      },
      setupNeuralNetwork() {
        let nnOptions = {
          dataUrl: './data/trainingdata.csv',
          inputs: ['salesRep','leadScore','customerAge','customerGender','customerCountry','customerEthnicity','companySize','companyIndustry'],
          outputs: ['result'],
          task: 'classification',
          debug: true
        };

        this.neuralNetwork = window.ml5.neuralNetwork(nnOptions, this.modelReady)
      }, 
      modelReady() {
        this.neuralNetwork.normalizeData();
        this.neuralNetwork.train({ epochs: 50 }, this.whileTraining, this.finishedTraining);
      }, 
      whileTraining(epoch, logs) {
        console.log(`Epoch: ${epoch} - loss: ${logs.loss.toFixed(2)}`);
      },
      finishedTraining() {
        console.log('Training completed!');
        this.isSetup = true; 
      },
      classify() {
        this.ranking = []; 
        this.salesreps.forEach(salesrep => {
          let salesRep = salesrep; 
          let leadScore = parseInt(this.scoreSelect);
          let customerAge = parseInt(this.ageSelect);
          let customerGender = this.genderSelect;
          let customerCountry = this.countrySelect;
          let customerEthnicity = this.ethnSelect;
          let companySize = parseInt(this.sizeSelect);
          let companyIndustry = this.industrySelect;
          let inputs = [salesRep, leadScore, customerAge, customerGender, customerCountry, customerEthnicity, companySize, companyIndustry];
          console.log(inputs); 
          try {
            this.neuralNetwork.classify(inputs, (err, results) => {
                if (err != undefined) {
                  console.log(err);
                } else {
                  console.log(salesrep + ": " + this.getProperty(results, 'success') + "%"); 
                  console.log(results);
                  this.updateRanking({name: salesrep, success: this.getProperty(results, 'success'), failure: this.getProperty(results, 'failure')});   
                }
            });
          } catch (error) {
            console.log('There was an error during the prediciton.');
            console.log('Please try correcting the input values and try again.'); 
            console.error(error);
          }
        }); 
      },
      getProperty(result, property) {
        return result.find(obj => {
          return obj.label === property
        }).confidence; 
      },
      updateRanking(newEntry) {
        //console.log('Ranking:'); 
        console.log(this.ranking); 
        this.ranking.push(newEntry); 
        this.ranking.sort((a, b) => (a.success < b.success) ? 1 : -1); 
        //select('#result').html(`Ideal sales rep: ${ranking[0].name} with ${ranking[0].success * 100}% chance to succeed.`);
      },
    },
    mounted() {
      this.setupNeuralNetwork();
    }
  }
</script>
