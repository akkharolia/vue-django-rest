<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4 offset-2">
        <h3> {{product_title}} </h3>
        <div>
            <p> {{ product_description }} </p>
            <p> Price : ${{ product_price }} </p>
          </div>
      </div>
      <div class="col-md-4" style="height:200px;">
        <img :src="product_image" alt="" height="100%">
      </div>
    </div>
    <div class="row ">
        <div class="col-md-3 offset-4">
          <button class=" btn btn-info btn-block mt-3 mb-4" @click="add_to_cart(product_id)">ADD TO CART</button>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert2';

let cart_products = [];
if(localStorage.getItem('cart_product')){
  cart_products = JSON.parse(localStorage.getItem('cart_product'))
}

export default {
  name: 'Product',
  data(){
    return {
      product_image:[],
      product_title: "",
      product_price:"",
      product_description:"",
      product_id: '',
      products: cart_products,
      token:'',
      auth_headers: {}
    }
  },
  mounted: function(){
    var auth_token = this.$session.get('token')
    this.token = 'JWT '+auth_token
    this.auth_headers = {headers: {'Authorization':this.token}}
    axios.get(`http://127.0.0.1:8000/api/product/${this.$route.params.id}`+'.json',this.auth_headers)
    .then(
      resp => {
        this.product_image = resp.data.image;
        this.product_title = resp.data.title;
        this.product_price = resp.data.price;
        this.product_id = resp.data.id;
        this.product_description = resp.data.description;
      }
    )
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
        this.products.push(response.data)
        swal.fire({icon:'success',title:'ADDED TO CART',timer:1500,position:'top-end',showConfirmButton: false,})
        localStorage.setItem('cart_product',JSON.stringify(this.products))
      }
    })
    }
  }
}
</script>