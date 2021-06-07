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
              <v-btn color="info" :large="$vuetify.breakpoint.smAndUp" @click="predict()">
                <v-icon left>mdi-cloud-upload</v-icon> Predict
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
      darkTheme: true,
      platformName: 'BIS3060',
      scoreSelect: null,
      ageSelect: null,
      genderSelect: null,
      genderItems: ['Male', 'Female'],
      countrySelect: null,
      countryItems: ['Germany', 'France', 'England', 'Poland'],
      ethnSelect: null,
      ethnItems: ['German', 'French', 'English', 'Polish'],
      sizeSelect: null,
      industrySelect: null, 
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
    },
  }
</script>
