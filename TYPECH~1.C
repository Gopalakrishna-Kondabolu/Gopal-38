#include <stdio.h>
#include <string.h>
#define MAX 100
// Symbol table entry
struct Symbol {
    char name[50];
    char type[10];
} symtab[MAX];
int count = 0;
// Insert into symbol table
void insert(char* name, char* type) {
int i;
    for ( i = 0; i < count; i++) {
	if (strcmp(symtab[i].name, name) == 0) {
	    printf("Variable '%s' already declared.\n", name);
	    return;
	}
    }
    strcpy(symtab[count].name, name);
    strcpy(symtab[count].type, type);
    count++;
}

// Get variable type
char* getType(char* name) {
int i;
    for ( i = 0; i < count; i++) {
	if (strcmp(symtab[i].name, name) == 0) {
	    return symtab[i].type;
	}
    }
    return NULL;
}
// Type compatibility check
int isCompatible(char* t1, char* t2, char* op) {
    if (strcmp(t1, t2) == 0)
	return 1;
    if ((strcmp(t1, "int") == 0 && strcmp(t2, "float") == 0) ||
	(strcmp(t1, "float") == 0 && strcmp(t2, "int") == 0))
	return 1;
    return 0;  // incompatible types
}
int main() {
    // Sample symbol table
    char var1[50], var2[50], op[5],*type1,*type2;

    insert("a", "int");
    insert("b", "float");
    insert("c", "int");
    // Sample expression: a + b
    printf("Enter expression (e.g., a + b): ");
    scanf("%s %s %s", var1, op, var2);
   type1=getType(var1);
   type2 = getType(var2);
    if (type1 == NULL || type2 == NULL) {
	printf("Error: Undeclared variable.\n");
	return 1;
    }
    printf("Type of '%s' = %s\n", var1, type1);
    printf("Type of '%s' = %s\n", var2, type2);

    if (isCompatible(type1, type2, op)) {
	printf("Types are compatible for '%s'\n", op);
    } else {
	printf("Type Error: Cannot apply '%s' to %s and %s\n", op, type1, type2);
    }

    return 0;
}
