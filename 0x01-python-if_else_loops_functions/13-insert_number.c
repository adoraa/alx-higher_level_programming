#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: ** of first node of listint_t list
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;
	prev = NULL;
	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	} else
	{
		new->next = current;
		prev->next = new;
	} return (new);
}
