import { Controller } from "@hotwired/stimulus"

// Connects to data-controller="hello"
export default class extends Controller {
  connect() {
    // この要素（<div>）の中にある<p>タグを見つけて、文字を書き換える
    this.element.querySelector('p').textContent = "JavaScriptが正常に動きました！🎉"
  }
}