#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: The first node in the list.
 * @n: The value of the new node.
 * Return: a pointer to the newelly inserted node.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, ;
	int i = 0;

	if (head == NULL)
		return (NULL);
	tmp = *head;
	for (; tmp->next and tmp->n <= number; tmp = tmp->next)
	{

	}
	
	return ()
}
