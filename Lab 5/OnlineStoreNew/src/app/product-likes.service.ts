import { Injectable } from '@angular/core';
import { Product } from './products';

@Injectable({
  providedIn: 'root'
})
export class ProductLikesService {
  constructor() { }

  toggleLike(product: Product): void {
    product.likes = product.likes > 0 ? 0 : 1;
  }

  isLiked(product: Product): boolean {
    return product.likes > 0;
  }
  
  deleteProduct(products: Product[], product: Product): Product[] {
    const index = products.findIndex(p => p.id === product.id);
    if (index !== -1) {
      return [...products.slice(0, index), ...products.slice(index + 1)];
    }
    return products;
  }
}
