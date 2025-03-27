import {Component, Input, OnInit} from '@angular/core';
import {Observable, share} from 'rxjs';
import { ProductLikesService } from '../product-likes.service';
import { Product } from '../products';

import { products } from '../products';
import {CartService} from "../cart.service";
import {Category} from "../categories";

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit{
  @Input() category!: Category

  constructor(private cartService: CartService, private likesService: ProductLikesService) { }
  shippingCosts!: Observable<{ type: string, price: number }[]>;

  share(url: string) {
    var sharelink = "https://t.me/share/url?url="+url;
    window.open(sharelink);
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }

  toggleLike(product: Product) {
    this.likesService.toggleLike(product);
  }
  
  isLiked(product: Product): boolean {
    return this.likesService.isLiked(product);
  }

  deleteProduct(product: Product) {
    if (confirm('Are you sure you want to delete this product?')) {
      this.category.products = this.likesService.deleteProduct(this.category.products, product);
    }
  }

  ngOnInit(): void {
    this.shippingCosts =  this.cartService.getShippingPrices();
  }
}
