import ICurrency from "./ICurrency";


export default interface ICurrencyRate {
  base: ICurrency,
  target: ICurrency,
  value: string
}