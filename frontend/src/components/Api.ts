import ICurrencyRate from "../config/ICurrencyRate";

function getCookie(name: string) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}


export default class Api {
  static async getCurrencies(): Promise<ICurrencyRate[]> {
    const response = await fetch(
      `/api`,
      {
        credentials: 'same-origin',
      }
    );
    return await response.json();
  }

  static async getRate(baseCurrency: string, targetCurrency: string, value: string): Promise<{result:string, success: boolean}> {
    const csrfToken: string = getCookie('csrftoken') || ''
    const formData = new FormData()
    formData.append('base_currency', baseCurrency)
    formData.append('target_currency', targetCurrency)
    formData.append('value', value)

    const response = await fetch(
      `/api/convert/`,
      {
        credentials: 'same-origin',
        method: 'POST',
        headers: {
          "CSRF": csrfToken
        },
        body: formData
      }
    );

    return response.json();
  }
}