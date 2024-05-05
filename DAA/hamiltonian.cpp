#include <iostream>
#define NODE 5
using namespace std;

int graph[NODE][NODE] = {
   {0, 1, 0, 1, 0},
   {1, 0, 1, 1, 1},
   {0, 1, 0, 0, 1},
   {1, 1, 0, 0, 1},
   {0, 1, 1, 1, 0},
};
int path[NODE];
// Function to display the Hamiltonian cycle
void displayCycle() {
   cout << "Cycle Found: ";
   for (int i = 0; i < NODE; i++)
      cout << path[i] << " ";
   // Print the first vertex again      
   cout << path[0] << endl; 
}
// Function to check if adding vertex v to the path is valid
bool isValid(int v, int k) {
   // If there is no edge between path[k-1] and v
   if (graph[path[k - 1]][v] == 0)
      return false;
   // Check if vertex v is already taken in the path
   for (int i = 0; i < k; i++)
      if (path[i] == v)
         return false;
   return true;
}
// function to find the Hamiltonian cycle
bool cycleFound(int k) {
   // When all vertices are in the path
   if (k == NODE) {
      // Check if there is an edge between the last and first vertex
      if (graph[path[k - 1]][path[0]] == 1)
         return true;
      else
         return false;
   }
   // adding each vertex to the path
   for (int v = 1; v < NODE; v++) {
      if (isValid(v, k)) {
         path[k] = v;
         if (cycleFound(k + 1) == true)
            return true;
         // Remove v from the path
         path[k] = -1;
      }
   }
   return false;
}
// Function to find and display the Hamiltonian cycle
bool hamiltonianCycle() {
   for (int i = 0; i < NODE; i++)
      path[i] = -1;
   // Set the first vertex as 0      
   path[0] = 0; 
   if (cycleFound(1) == false) {
      cout << "Solution does not exist" << endl;
      return false;
   }
   displayCycle();
   return true;
}
int main() {
   hamiltonianCycle();
}