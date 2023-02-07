def solve():
    n = float(input())
    cem = n // 100
    cinquenta = n % 100
    vinte = cinquenta % 50
    dez = vinte % 20
    cinco = dez % 10
    dois = cinco % 5
    cedulas = {
        100: cem * 100,
        50: (cinquenta // 50) * 50,
        10: (vinte // 20) * 20,
        5: (cinco // 5) * 5,
        2: (dois // 2) * 2,
    }
    troco = n - sum(cedulas.values())
    um_real = troco // 1.00
    cinquenta_centavos = troco % 1.00
    vinte_e_cinco_centavos = cinquenta_centavos % 0.50
    dez_centavos = vinte_e_cinco_centavos % 0.25
    cinco_centavos = dez_centavos % 0.10
    um_centavo = cinco_centavos % 0.05
    print(
        "NOTAS:",
        f"{int(cem)} nota(s) de R$ 100.00",
        f"{int(cinquenta//50)} nota(s) de R$ 50.00",
        f"{int(vinte//20)} nota(s) de R$ 20.00",
        f"{int(dez//10)} nota(s) de R$ 10.00",
        f"{int(cinco//5)} nota(s) de R$ 5.00",
        f"{int(dois//2)} nota(s) de R$ 2.00",
        "MOEDAS:",
        f"{int(um_real)} moeda(s) de R$ 1.00",
        f"{int(cinquenta_centavos//0.50)} moeda(s) de R$ 0.50",
        f"{int(vinte_e_cinco_centavos//0.25)} moeda(s) de R$ 0.25",
        f"{int(dez_centavos//0.10)} moeda(s) de R$ 0.10",
        f"{int(cinco_centavos//0.05)} moeda(s) de R$ 0.05",
        f"{int(um_centavo//0.01)} moeda(s) de R$ 0.01",
        sep="\n",
    )


if __name__ == "__main__":
    solve()
