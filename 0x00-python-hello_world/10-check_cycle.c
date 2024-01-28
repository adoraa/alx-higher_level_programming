#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: returns 1 if there is a cycle, else returns 0
 */
int check_cycle(listint_t *list)
{
	listint_t *walk = list;
	listint_t *jump = list;

	while (walk && jump && jump->next)
	{
		walk = walk->next;
		jump = jump->next->next;

		if (walk == jump)
			return (1);
	}
	return (0);
}
