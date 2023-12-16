class Solution {
    fun destCity(paths: List<List<String>>): String {
        var city:String = paths[0][0]
        val pathsMaps: MutableMap<String, String> = mutableMapOf()
        for (singlePath in paths) {
            print(singlePath)
            val sta = singlePath[0]
            val des = singlePath[1]
            pathsMaps.put(sta, des)
        }

        while (pathsMaps.containsKey(city)) {
            city = pathsMaps[city]!!
        }
        return city
    }
}