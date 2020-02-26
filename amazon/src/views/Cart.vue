<template>
  <div>
    <div class="title">
      <h1>{{msg}}</h1>
      <div class="container mt-4 pb-5">
        <div class="row" v-for="(data,n) in cart_product" :key="data.id">
          <div class="col-md-10 border offset-1">
            <div class="row pt-3" style="line-height:50px">
              <div class="col-md-1" > 
                <span class="text-small btn btn-small btn-info">{{numbers}}</span>
              </div>
              <div class="col-md-2" > 
                <p class=" text-small float-left"><router-link :to="{ path: '/product_info/'+ data.id}">{{data.title}}</router-link></p>
              </div>
              <div class="col-md-1 text-small">
                <p>${{data.price}}</p>
              </div>
              <div class="col-md-2">
                <img :src="data.image" class="pb-3" width="50px">
              </div>
              <div class="col-md-2">
                <button class="btn btn-sm btn-info mr-3" @click="changeQuantity(data,'decrease')">-</button> 
                <span>{{data.quantity}}</span>
                <button class="btn btn-sm btn-info ml-3" @click="changeQuantity(data,'increase')">+</button> 
              </div>
              <div class="col-md-2 text-small">
                Total: ${{ data.price*data.quantity }}
              </div>
              <div class="col-md-2">
                <button class="btn btn-danger btn-sm" @click="removeCart(n)"><i class="material-icons pt-2">delete</i></button> 
              </div>
            </div>
          </div>
        </div>
        <div class="row mt-4">
          <div class="col-md-7"></div>
          <div class="col-md-2 float-right">
            <h6>Cart Total : ${{total}} </h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
// import axios from 'axios'
  export default {
    name: 'Cart',
    data: () => ({
      msg: 'Welcome to Cart Page',
      cart_product: JSON.parse(localStorage.getItem("cart_product")),
      numbers:1,
      total: 0,
    }),
    mounted(){
      for (let i = 0; i < this.cart_product.length; i++) {
      const product_price = this.cart_product[i]['price'];
      const product_quantity = this.cart_product[i]['quantity'];
      this.total += product_price*product_quantity
      }
      return this.total;
      
    },
    methods: {
    removeCart(n) { 
      this.cart_product.splice(n,1);
      if(this.cart_product.length == 0){
        localStorage.removeItem('cart_product')
      }
      else{
        localStorage.setItem('cart_product',JSON.stringify(this.cart_product))
      }
      
    },
    changeQuantity(itemToAdd, operation){
      let itemInCart = this.cart_product.filter(item => item.id===itemToAdd.id)
      if(operation == 'increase'){
        JSON.parse(localStorage.getItem("cart_product"))
        itemInCart[0].quantity += 1
        localStorage.setItem('cart_product',JSON.stringify(this.cart_product))
        this.total += itemInCart[0].price
        
      }else {
      if(operation == 'decrease'){
        if(itemInCart[0].quantity==1){
          this.cart_product.splice(this.cart_product.indexOf(itemToAdd.id,1))
          localStorage.setItem('cart_product',JSON.stringify(this.cart_product))
          this.total -= itemInCart[0].price
        } else {
          itemInCart[0].quantity -= 1
          localStorage.setItem('cart_product',JSON.stringify(this.cart_product))
          this.total -= itemInCart[0].price
        }
      }}
      
    }
    },
  }
</script>

<style scoped>
.text-small{
  font-size:12px
}
</style>