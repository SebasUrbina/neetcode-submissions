class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = XYYZ
        k =
        uppersLetters -> 26 (A->Z)

        Necesito encontrar la subcadena mas larga tal que luego de hacer 
        hasta k reemplazos solo contiene un tipo de char.

        XYYX -> k=2 => Valdia, res = 4

        Invariante: # Cambios = Tamaño de ventana - frecuencia maxima: 2
        Necesito iterar en la ventana usando Two Pointers.
        Cuando la ventana sea valida -> continuo
        Cuando la ventana sea invalida -> me muevo hasta que sea valida.
        """

        counts = {} # {'A': count(A), 'B': count(B)}
        res = 0 # maxLength
        l = 0 
        for r in range(len(s)): 
            counts[s[r]] = 1 + counts.get(s[r], 0) # increment counter
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1 # we move the left pointer to right.
                l += 1
            
            res = max(res, (r - l + 1))

        return res
        