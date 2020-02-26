<template>
  <div class="hello">
    <h3 class="mb-5">{{ msg }}</h3>
  <div class="container">
    <div class="row">
        <div class="col-md-3 offset-4 mb-5">
          <select name="orderby" class="form-control" @change="sortBy($event)">
          <option value="title_asc">Sort by Name: Ascending</option>
          <option value="title_desc">Sort by Name: Descending</option>
          <option value="price_asc">Sort by price: low to high</option>
          <option value="price_desc">Sort by price: high to low</option>
          </select>
          </div>
      </div>
    <div class="row">
    <div class="col-md-4 p-2 border" v-for="text in info" :key="text.id">
      <div class="product" style="height:220px;overflow:hidden">
        <div class="row">
          <div class="col-md-12"><div style="font-weight:bold"> {{text.title}}  </div></div>
        </div>
        <div class="row">
          <div class="col-md-12"><span style="font-weight:bold" > ${{text.price}} </span></div>
        </div>
          <div class="row">
            <div class="col-md-5">
                {{text.description}}
              </div>
            <div class="col-md-7">
              <img :src="text.image" alt="" class="fit-image">
              </div>
            </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-5">
                <button class=" float-left btn btn-info btn-sm" @click="add_to_cart(text.id)">ADD TO CART </button>
              </div>
              <div class="col-md-2"></div>
              <div class="col-md-5">
              <router-link :to="{ path: '/product_info/'+ text.id}"> 
                <button class=" btn btn-info btn-sm">VIEW PRODUCT</button>
              </router-link>
              </div>
            </div>
      </div>
    </div>
    <div class="row mt-3 mb-2">
      <div class="col-md-12">
        <ul class="list-horizontal">
          <li>
            <button class="btn btn-primary btn-sm mx-3" @click="getPrevPage()" v-if="prev_page_url != null">Previous Page
            </button>
            <button class="btn btn-primary btn-sm mx-3" @click="getNextPage()" v-if="next_page_url != null">Next Page
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from "../router";
import swal from 'sweetalert2';


let cart_products = [];
if(localStorage.getItem('cart_product')){
  cart_products = JSON.parse(localStorage.getItem('cart_product'))
}
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },

  data: () => ({
      info: '',
      products: cart_products,
      quantity: 0,
      next_page_url:'',
      prev_page_url:'',
      loading: false,
      resp_data:'',
      token:'',
      auth_headers: {}
    }),
    mounted () {
      var auth_token = this.$session.get('token')
      axios.post('http://127.0.0.1:8000/api/auth/refresh_token/',{'token':auth_token})
      .then(resp => {
        this.$session.set('token', resp.data.token);
      })
      this.token = 'JWT '+auth_token
      this.auth_headers = {headers: {'Authorization':this.token}}      
      let cart_products = [];
      if(localStorage.getItem('cart_product')){
        cart_products = JSON.parse(localStorage.getItem('cart_product'))
      }
      this.products = cart_products;
      axios.get('http://127.0.0.1:8000/api/product/?ordering=title',this.auth_headers)
      .then(resp => {      
        this.resp_data = resp.data
        this.info = resp.data.results
        this.next_page_url = resp.data.next
        this.prev_page_url = resp.data.previous
      }
    );
    this.checkLoggedIn();
        
  },

  methods: {
    add_to_cart(cart_id) {      
    axios.get(`http://localhost:8000/api/product/${cart_id}.json`,this.auth_headers)
    .then(response => {
      if (!response.data) {
        return;
      }
      if (this.products.find(p => p.id === cart_id)) {
        swal.fire({icon:'error',text:'This product already in your cart.',timer:1500,position:'top-end',showConfirmButton: false,})
      } else {
        JSON.parse(localStorage.getItem('cart_product'))
        this.products.push(response.data)
        swal.fire({icon:'success',title:'ADDED TO CART',timer:1500,position:'top-end',showConfirmButton: false,})
        localStorage.setItem('cart_product',JSON.stringify(this.products))
      }
    })
    },
    sortBy(event){
      if(event.target.value == 'title_desc'){
        axios.get('http://127.0.0.1:8000/api/product/?ordering=-title',this.auth_headers)
        .then(resp => {
          this.info = resp.data.results
          this.resp_data = resp.data
          this.next_page_url = resp.data.next
          this.prev_page_url = resp.data.previous
        }
      )
      }
      if(event.target.value == 'title_asc'){
        axios.get('http://127.0.0.1:8000/api/product/?ordering=title',this.auth_headers)
        .then(resp => {
          this.info = resp.data.results
          this.resp_data = resp.data
          this.next_page_url = resp.data.next
          this.prev_page_url = resp.data.previous
        }
      )
      }
      if(event.target.value == 'price_desc'){
        axios.get('http://127.0.0.1:8000/api/product/?ordering=-price',this.auth_headers)
        .then(resp => {
          this.info = resp.data.results
          this.resp_data = resp.data
          this.next_page_url = resp.data.next
          this.prev_page_url = resp.data.previous
        }
      )
      }
      if(event.target.value == 'price_asc'){
        axios.get('http://127.0.0.1:8000/api/product/?ordering=price',this.auth_headers)
        .then(resp => {
          this.info = resp.data.results
          this.resp_data = resp.data
          this.next_page_url = resp.data.next
          this.prev_page_url = resp.data.previous
        }
      )
      }
    },
    getPrevPage(){
      axios.get(this.prev_page_url,this.auth_headers).then(response => {
        this.resp_data = response.data
        this.info = response.data.results
        this.next_page_url = response.data.next
        this.prev_page_url = response.data.previous
      })
    },
    getNextPage(){
      axios.get(this.next_page_url,this.auth_headers).then(response => {
        this.resp_data = response.data
        this.info = response.data.results
        this.next_page_url = response.data.next
        this.prev_page_url = response.data.previous
      })
    },
    checkLoggedIn() {      
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/login");
      }
    }
  }
}
</script>

<style scoped lang="scss">
h3 {
  margin: 10px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: white;
}
.fit-image{
width: 100%;
// height: 40%;
object-fit: cover;
// height: 300px; /* only if you want fixed height */
}
</style>
