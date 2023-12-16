class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        val sArr: List<Char> = s.toList().sorted()
        val tArr: List<Char> = t.toList().sorted()

        print(sArr)
        print(tArr)
        return sArr == tArr
    }
}