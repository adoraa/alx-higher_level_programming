#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: returns 1 if the list is a palindrome, else returns 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *arr, size = 0, i;

	while (current)
	{
		size++;
		current = current->next;
	} arr = malloc(size * sizeof(int));
	if (arr == NULL)
		return (0);
	current = *head;
	for (i = 0; i < size; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}
	for (i = 0; i < size / 2; i++)
	{
		if (arr[i] != arr[size - 1 - i])
		{
			free(arr);
			return (0);
		}
	} free(arr);
	return (1);
}
