public class TwoSum {
    public static int[] findTwoSum(int[] list, int sum) {
        
        for(int i: list){
            for(int j=1; j<list.size())
            if(i+(i+1)==sum){
                
            }
        }
        
        throw new UnsupportedOperationException("Waiting to be implemented.");
    }

    public static void main(String[] args) {
        int[] indices = findTwoSum(new int[] { 3, 1, 5, 7, 5, 9 }, 10);
        if(indices != null) {
            System.out.println(indices[0] + " " + indices[1]);
        }
    }
}